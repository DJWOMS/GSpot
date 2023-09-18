'use client'

import { FC, useState } from 'react'
import { Controller, useForm } from 'react-hook-form'
import { ErrorMessage } from '@hookform/error-message'
import { Input } from 'components/Form'
import type { UserDataInterface } from 'features/profile/types'
import { fetchServerSide } from 'lib/fetchServerSide'
import s from '../page.module.css'

interface InputTypes {
  username: string
  email: string
  firstName: string
  lastName: string
}

interface Props {
  data?: UserDataInterface
}

const ProfileForm: FC<Props> = ({ data }) => {
  const [saved, setSaved] = useState(false)
  const [error, setError] = useState<false | string>(false)

  const {
    formState: { errors, isValid },
    handleSubmit,
    control,
  } = useForm<InputTypes>({
    defaultValues: data
      ? data
      : {
          username: '',
          email: '',
          firstName: '',
          lastName: '',
        },
    mode: 'onBlur',
  })

  const onSubmitUser = async (data: InputTypes) => {
    setSaved(false)
    setError(false)
    const response = await fetchServerSide<UserDataInterface>({
      path: '/profile/settings',
      method: 'POST',
      body: JSON.stringify(data) as string,
    })
    if (response) {
      if (response.status === 400) setError('пользователь существует')
      if (response.status === 201) {
        setSaved(true)
        setTimeout(() => setSaved(false), 3000)
      }
    }
  }
  const errorMessage = 'Минимум 3 символовa'

  return (
    <form action="#" className={s.form} onSubmit={handleSubmit(onSubmitUser)}>
      <h4 className={s.formTitle}>Настройки профиля</h4>
      <div className={s.col}>
        <div>
          <label className={s.formLabel} htmlFor="username">
            Ник
          </label>
          <Controller
            name="username"
            control={control}
            rules={{
              required: true,
              minLength: {
                value: 3,
                message: errorMessage,
              },
            }}
            render={({ field }) => <Input {...field} type="text" placeholder="Doe" />}
          />
          <ErrorMessage
            errors={errors}
            name="username"
            render={({ message }) => <p className={s.errorMessage}>{message}</p>}
          />
        </div>
        <div>
          <label className={s.formLabel} htmlFor="email">
            Email
          </label>
          <Controller
            name="email"
            control={control}
            rules={{
              required: true,
              minLength: {
                value: 3,
                message: errorMessage,
              },
            }}
            render={({ field }) => <Input {...field} type="text" placeholder="email@email.com" />}
          />
          <ErrorMessage
            errors={errors}
            name="email"
            render={({ message }) => <p className={s.errorMessage}>{message}</p>}
          />
        </div>
        <div>
          <label className={s.formLabel} htmlFor="firstName">
            Имя
          </label>
          <Controller
            name="firstName"
            control={control}
            rules={{
              required: true,
              minLength: {
                value: 3,
                message: errorMessage,
              },
            }}
            render={({ field }) => <Input {...field} type="text" placeholder="John" />}
          />
          <ErrorMessage
            errors={errors}
            name="firstName"
            render={({ message }) => <p className={s.errorMessage}>{message}</p>}
          />
        </div>
        <div>
          <label className={s.formLabel} htmlFor="lastName">
            Фaмилия
          </label>
          <Controller
            name="lastName"
            control={control}
            rules={{
              required: true,
              minLength: {
                value: 3,
                message: errorMessage,
              },
            }}
            render={({ field }) => <Input {...field} type="text" placeholder="Doe" />}
          />
          <ErrorMessage
            errors={errors}
            name="lastName"
            render={({ message }) => <p className={s.errorMessage}>{message}</p>}
          />
        </div>
      </div>
      {error && <p className={s.errorMessage}>{error}</p>}
      {saved && <p className={s.saved}>Сохранено</p>}
      <input className={s.formBtn} type="submit" value="сохранить" disabled={!isValid} />
    </form>
  )
}

export default ProfileForm
