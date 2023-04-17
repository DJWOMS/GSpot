'use client'

import { useEffect, useState } from 'react'
import { useForm } from 'react-hook-form'
import { UserDataInterface } from 'features/profile'
import { fetchServerSide } from 'lib/fetchServerSide'
import Profile from './Profile'
import s from './page.module.scss'

interface InputTypes {
  oldPassword: string
  newPassword: string
  confirmPassword: string
}

const Settings = () => {
  const [pass, setPass] = useState<string | null>()
  // useEffect(()=> {},[])
  const {
    register,
    formState: { errors, isValid },
    handleSubmit,
    reset,
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

  const onSubmitPasword = (data: any) => {
    if (data.newPassword === data.confirmPassword) {
      const res = validatePassword(data.newPassword)
      if (res) {
        setPass(null)
        alert(JSON.stringify(data))
      } else {
        setPass('пароль слишком легкий')
      }
    } else {
      setPass('пароли не совпадают')
    }
    reset()
  }

  return (
    <div className={s.row}>
      {/* @ts-expect-error Async Server Component */}
      <Profile />
      <form action="#" className={s.form} onSubmit={handleSubmit(onSubmitPasword)}>
        <h4 className={s.formTitle}>Поменять пароль</h4>
        <p className={s.formPassword}>{pass}</p>

        <div className={s.col}>
          <div>
            <label className={s.formLabel} htmlFor="oldpass">
              Старый пароль
            </label>
            <input
              {...register('oldPassword', {
                required: 'поле не заполнено',
              })}
              id="oldpass"
              type="password"
              className={s.formInput}
              placeholder="***"
            />
            {errors?.oldPassword && <span style={{ color: 'red' }}>поле не заполненно</span>}
          </div>
          <div>
            <label className={s.formLabel} htmlFor="newpass">
              Новый пароль
            </label>
            <input
              {...register('newPassword', {
                required: 'поле не заполнено',
              })}
              id="oldpass"
              type="password"
              className={s.formInput}
              placeholder="***"
            />
            {errors?.newPassword && <span style={{ color: 'red' }}>поле не заполненно</span>}
          </div>
          <div>
            <label className={s.formLabel} htmlFor="confirmpass">
              Подтвердить Новый пароль
            </label>
            <input
              {...register('confirmPassword', {
                required: 'поле не заполнено',
                minLength: {
                  value: 3,
                  message: 'Минимум 3 символовa',
                },
              })}
              id="oldpass"
              type="password"
              className={s.formInput}
              placeholder="***"
            />
            {errors?.confirmPassword && <span style={{ color: 'red' }}>{errors?.confirmPassword?.message || 'поле не заполненно'}</span>}
          </div>
        </div>
        <input type="submit" className={s.formBtn} value="Поменять" disabled={!isValid} />
      </form>
    </div>
  )
}

export default Settings
