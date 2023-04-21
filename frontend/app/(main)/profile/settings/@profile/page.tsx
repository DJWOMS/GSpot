'use client'

import { useEffect, useState } from 'react'
import { Controller, useForm } from 'react-hook-form'
import { ErrorMessage } from '@hookform/error-message'
import { Input } from 'components/Form'
import { SkeletonInput } from 'components/Skeleton'
import { UserDataInterface } from 'features/profile'
import { fetchServerSide } from 'lib/fetchServerSide'
import s from '../page.module.scss'

interface InputTypes {
  username: string
  email: string
  firstName: string
  lastName: string
}
const Profile = () => {
  const [saved, setSaved] = useState(false)
  const [error, setError] = useState<false | string>(false)
  const {
    formState: { errors, isValid, isLoading },
    handleSubmit,
    control,
  } = useForm<InputTypes>({
    defaultValues: async () => {
      const data = await fetchServerSide<UserDataInterface | undefined>({
        path: '/profile/settings',
      })
      if (data) {
        return {
          username: data.username,
          email: data.email,
          firstName: data.firstName,
          lastName: data.lastName,
        }
      }
      return {
        username: '',
        email: '',
        firstName: '',
        lastName: '',
      }
    },
    mode: 'onBlur',
  })
  const onSubmitUser = async (data: any) => {
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
          {isLoading ? (
            <SkeletonInput height="44px" />
          ) : (
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
          )}
          <ErrorMessage errors={errors} name="username" render={({ message }) => <p className={s.errorMessage}>{message}</p>} />
        </div>
        <div>
          <label className={s.formLabel} htmlFor="email">
            Email
          </label>
          {isLoading ? (
            <SkeletonInput height="44px" />
          ) : (
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
          )}
          <ErrorMessage errors={errors} name="email" render={({ message }) => <p className={s.errorMessage}>{message}</p>} />
        </div>
        <div>
          <label className={s.formLabel} htmlFor="firstName">
            Имя
          </label>
          {isLoading ? (
            <SkeletonInput height="44px" />
          ) : (
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
          )}
          <ErrorMessage errors={errors} name="firstName" render={({ message }) => <p className={s.errorMessage}>{message}</p>} />
        </div>
        <div>
          <label className={s.formLabel} htmlFor="lastName">
            Фaмилия
          </label>
          {isLoading ? (
            <SkeletonInput height="44px" />
          ) : (
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
          )}
          <ErrorMessage errors={errors} name="lastName" render={({ message }) => <p className={s.errorMessage}>{message}</p>} />
        </div>
      </div>
      {error && <p className={s.errorMessage}>{error}</p>}
      {saved && <p className={s.saved}>Сохраненно</p>}
      <input className={s.formBtn} type="submit" value="сохранить" disabled={!isValid} />
    </form>
  )
}

export default Profile
