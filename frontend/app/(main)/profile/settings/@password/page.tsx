'use client'

import { useState } from 'react'
import { Controller, useForm } from 'react-hook-form'
import { ErrorMessage } from '@hookform/error-message'
import { Input } from 'components/Form'
import { SkeletonInput } from 'components/Skeleton'
import { fetchServerSide } from 'lib/fetchServerSide'
import s from '../page.module.css'

interface InputTypes {
  oldPassword: string
  newPassword: string
  confirmPassword: string
}

const Password = () => {
  const [saved, setSaved] = useState(false)
  const {
    handleSubmit,
    reset,
    control,
    formState: { errors, isValid, isLoading },
  } = useForm<InputTypes>({
    mode: 'onBlur',
    defaultValues: {
      oldPassword: '',
      newPassword: '',
      confirmPassword: '',
    },
  })

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
    reset()
  }

  const errorMessage = 'поле не заполнено'

  return (
    <form action="#" className={s.form} onSubmit={handleSubmit(onSubmitPassword)}>
      <h4 className={s.formTitle}>Поменять пароль</h4>
      <div className={s.col}>
        <div>
          <label className={s.formLabel} htmlFor="oldPassword">
            Старый пароль
          </label>
          {isLoading ? (
            <SkeletonInput height="44px" />
          ) : (
            <Controller
              name="oldPassword"
              control={control}
              rules={{
                required: true,
                minLength: {
                  value: 3,
                  message: errorMessage,
                },
              }}
              render={({ field }) => (
                <Input {...field} id="oldPassword" type="password" placeholder="*** *** ***" />
              )}
            />
          )}
          <ErrorMessage
            errors={errors}
            name="oldPassword"
            render={({ message }) => <p className={s.errorMessage}>{message}</p>}
          />
        </div>
        <div>
          <label className={s.formLabel} htmlFor="newPassword">
            Новый пароль
          </label>
          {isLoading ? (
            <SkeletonInput height="44px" />
          ) : (
            <Controller
              name="newPassword"
              control={control}
              rules={{
                required: true,
                minLength: {
                  value: 3,
                  message: errorMessage,
                },
                validate: (value) => validatePassword(value) || 'пароль слишком легкий',
              }}
              render={({ field }) => (
                <Input {...field} id="newPassword" type="password" placeholder="*** *** ***" />
              )}
            />
          )}
          <ErrorMessage
            errors={errors}
            name="newPassword"
            render={({ message }) => <p className={s.errorMessage}>{message}</p>}
          />
        </div>
        <div>
          <label className={s.formLabel} htmlFor="confirmPassword">
            Подтвердить Новый пароль
          </label>
          {isLoading ? (
            <SkeletonInput height="44px" />
          ) : (
            <Controller
              name="confirmPassword"
              control={control}
              rules={{
                required: true,
                minLength: {
                  value: 3,
                  message: errorMessage,
                },
                validate: (value, formValues) => value === formValues.newPassword || 'пароли не совпадают',
              }}
              render={({ field }) => (
                <Input {...field} id="confirmPassword" type="password" placeholder="*** *** ***" />
              )}
            />
          )}
          <ErrorMessage
            errors={errors}
            name="confirmPassword"
            render={({ message }) => <p className={s.errorMessage}>{message}</p>}
          />
        </div>
      </div>
      {saved && <p className={s.saved}>Пароль изменен</p>}
      <input type="submit" className={s.formBtn} value="Поменять" disabled={!isValid} />
    </form>
  )
}

export default Password
