'use client'

import { useEffect, useState } from 'react'
import { useForm } from 'react-hook-form'
import { ErrorMessage } from '@hookform/error-message'
import { UserDataInterface } from 'features/profile'
import { fetchServerSide } from 'lib/fetchServerSide'
import s from '../page.module.scss'

interface InputTypes {
  nickName: string
  email: string
  firstName: string
  lastName: string
}
const Profile = () => {
  const [saved, setSaved] = useState(false)
  const {
    register,
    formState: { errors, isValid },
    handleSubmit,
    setValue,
  } = useForm<InputTypes>({
    mode: 'onBlur',
  })

  useEffect(() => {
    const loadData = async () => {
      const response = await fetchServerSide<UserDataInterface>({
        path: '/profile/settings',
      })
      if (response) {
        setValue('nickName', response.nickName)
        setValue('email', response.email)
        setValue('firstName', response.firstName)
        setValue('lastName', response.lastName)
      }
    }
    loadData()
  }, [])

  const onSubmitUser = async (data: any) => {
    setSaved(false)
    const response = await fetchServerSide<UserDataInterface>({
      path: '/profile/settings',
      method: 'POST',
      body: JSON.stringify(data) as string,
    })
    if (response) setSaved(true)
  }
  const errorMassage = 'Минимум 3 символовa'

  return (
    <form action="#" className={s.form} onSubmit={handleSubmit(onSubmitUser)}>
      <h4 className={s.formTitle}>Настройки профиля</h4>

      <div className={s.col}>
        <div>
          <label className={s.formLabel} htmlFor="nickName">
            Ник
          </label>
          <input
            {...register('nickName', {
              required: true,
              minLength: {
                value: 3,
                message: errorMassage,
              },
            })}
            className={s.formInput}
            placeholder="Doe"
          />
          <ErrorMessage errors={errors} name="nickName" render={({ message }) => <p className={s.errorMessage}>{message}</p>} />
        </div>
        <div>
          <label className={s.formLabel} htmlFor="email">
            Email
          </label>
          <input
            {...register('email', {
              required: true,
              minLength: {
                value: 3,
                message: errorMassage,
              },
            })}
            className={s.formInput}
            placeholder="email@email.com"
          />
          <ErrorMessage errors={errors} name="email" render={({ message }) => <p className={s.errorMessage}>{message}</p>} />
        </div>

        <div>
          <label className={s.formLabel} htmlFor="firstName">
            Имя
          </label>
          <input
            {...register('firstName', {
              required: true,
              minLength: {
                value: 3,
                message: errorMassage,
              },
            })}
            className={s.formInput}
            placeholder="John"
          />
          <ErrorMessage errors={errors} name="firstName" render={({ message }) => <p className={s.errorMessage}>{message}</p>} />
        </div>

        <div>
          <label className={s.formLabel} htmlFor="lastName">
            Фaмилия
          </label>
          <input
            {...register('lastName', {
              required: true,
              minLength: {
                value: 3,
                message: errorMassage,
              },
            })}
            className={s.formInput}
            placeholder="Doe"
          />
          <ErrorMessage errors={errors} name="lastName" render={({ message }) => <p className={s.errorMessage}>{message}</p>} />
        </div>
      </div>
      {saved && <p className={s.saved}>Сохраненно</p>}
      <input className={s.formBtn} type="submit" value="сохранить" disabled={!isValid} />
    </form>
  )
}

export default Profile
