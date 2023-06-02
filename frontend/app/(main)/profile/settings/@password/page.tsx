'use client'

import { useState } from 'react'
import { useForm } from 'react-hook-form'
import Form from 'components/Form/Form'
import { fetchServerSide } from 'lib/fetchServerSide'
import s from '../page.module.css'

interface InputTypes {
  oldPassword: string
  newPassword: string
  confirmPassword: string
}

const Password = () => {
  const [saved, setSaved] = useState(false)

  function validatePassword(password: string): boolean {
    return (
      password.length >= 8 &&
      /[a-z]/.test(password) &&
      /[A-Z]/.test(password) &&
      /\d/.test(password) &&
      // eslint-disable-next-line
      /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(password)
    )
  }

  const onSubmitPassword = async (data: InputTypes) => {
    setSaved(false)
    const response = await fetchServerSide<InputTypes>({
      path: '/profile/settings/password',
      method: 'POST',
      body: JSON.stringify(data) as string,
    })
    if (response) {
      setSaved(true)
      setTimeout(() => setSaved(false), 3000)
    }
  }

  return (
    <Form
      fields={[
        {
          name: 'oldPassword',
          label: 'Старый пароль',
          rules: {
            required: true,
            minLength: {
              value: 3,
              message: 'Введите старый пароль',
            },
          },
          render: ({ field }) => (
            <input
              {...field}
              id="oldPassword"
              type="password"
              placeholder="*** *** ***"
              className={s.formInput}
            />
          ),
        },
        {
          name: 'newPassword',
          label: 'Новый пароль',
          rules: {
            required: true,
            minLength: {
              value: 3,
              message: 'Введите новый пароль',
            },
            validate: (value) => validatePassword(value) || 'пароль слишком легкий',
          },
          render: ({ field }) => (
            <input
              {...field}
              id="newPassword"
              type="password"
              placeholder="*** *** ***"
              className={s.formInput}
            />
          ),
        },
        {
          name: 'confirmPassword',
          label: 'Подтвердить Новый пароль',
          rules: {
            required: true,
            minLength: {
              value: 3,
              message: 'Введите подтверждение нового пароля',
            },
            validate: (value, formValues) => value === formValues.newPassword || 'пароли не совпадают',
          },
          render: ({ field }) => (
            <input
              {...field}
              id="confirmPassword"
              type="password"
              placeholder="*** *** ***"
              className={s.formInput}
            />
          ),
        },
      ]}
      title="Поменять пароль"
      onSubmit={onSubmitPassword}
      btnText="Поменять"
      onResetSubmit
      config={{
        mode: 'onChange',
        defaultValues: {
          oldPassword: '',
          newPassword: '',
          confirmPassword: '',
        },
      }}
    />
  )
}

export default Password
