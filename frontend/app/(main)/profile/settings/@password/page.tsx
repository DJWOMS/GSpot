'use client'

import { useState } from 'react'
import { useForm } from 'react-hook-form'
import { ErrorMessage } from '@hookform/error-message'
import { fetchServerSide } from 'lib/fetchServerSide'
import s from '../page.module.scss'

interface InputTypes {
  oldPassword: string
  newPassword: string
  confirmPassword: string
  change?: string
}

const Password = () => {
  const [pass, setPass] = useState<string | null>()
  const [saved, setSaved] = useState(false)
  const {
    register,
    formState: { errors, isValid },
    handleSubmit,
    reset,
    setValue,
  } = useForm<InputTypes>({
    mode: 'onBlur',
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

  const onSubmitPasword = async (data: any) => {
    setSaved(false)
    if (data.newPassword === data.confirmPassword) {
      const res = validatePassword(data.newPassword)
      if (res) {
        setPass(null)
        const response = await fetchServerSide<InputTypes>({
          path: '/profile/settings/password',
          method: 'POST',
          body: JSON.stringify(data) as string,
        })
        if (response) {
          setValue('change', response.change)
          setSaved(true)
        }
      } else {
        setPass('пароль слишком легкий')
      }
    } else {
      setPass('пароли не совпадают')
    }
    reset()
  }

  const errorMessage = 'поле не заполнено'

  return (
    <form action="#" className={s.form} onSubmit={handleSubmit(onSubmitPasword)}>
      <h4 className={s.formTitle}>Поменять пароль</h4>
      <p className={s.formPassword}>{pass}</p>

      <div className={s.col}>
        <div>
          <label className={s.formLabel} htmlFor="oldPassword">
            Старый пароль
          </label>
          <input
            {...register('oldPassword', {
              required: errorMessage,
            })}
            id="oldpass"
            type="password"
            className={s.formInput}
            placeholder="*** *** ***"
          />
          <ErrorMessage errors={errors} name="oldPassword" render={({ message }) => <p className={s.errorMessage}>{message}</p>} />
        </div>
        <div>
          <label className={s.formLabel} htmlFor="newPassword">
            Новый пароль
          </label>
          <input
            {...register('newPassword', {
              required: errorMessage,
            })}
            id="oldpass"
            type="password"
            className={s.formInput}
            placeholder="*** *** ***"
          />
          <ErrorMessage errors={errors} name="newPassword" render={({ message }) => <p className={s.errorMessage}>{message}</p>} />
        </div>
        <div>
          <label className={s.formLabel} htmlFor="confirmPassword">
            Подтвердить Новый пароль
          </label>
          <input
            {...register('confirmPassword', {
              required: errorMessage,
              minLength: {
                value: 3,
                message: errorMessage,
              },
            })}
            id="oldpass"
            type="password"
            className={s.formInput}
            placeholder="*** *** ***"
          />
          <ErrorMessage errors={errors} name="confirmPassword" render={({ message }) => <p className={s.errorMessage}>{message}</p>} />
        </div>
      </div>
      {saved && <p className={s.saved}>Пароль изменен</p>}
      <input type="submit" className={s.formBtn} value="Поменять" disabled={!isValid} />
    </form>
  )
}

export default Password
