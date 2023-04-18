import { useEffect } from 'react'
import { useForm } from 'react-hook-form'
import { UserDataInterface } from 'features/profile'
import { fetchServerSide } from 'lib/fetchServerSide'
import s from './page.module.scss'

interface InputTypes {
  nickName: string
  email: string
  firstName: string
  lastName: string
}
const Profile = () => {
  const {
    register,
    formState: { errors, isValid },
    handleSubmit,
    reset,
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
    // alert(JSON.stringify(data))
    const response = await fetchServerSide<UserDataInterface>({
      path: '/profile/settings',
      method: 'POST',
      body: data,
      headers: {
        'Content-Type': 'application/json',
      },
    })
    if (response) {
      setValue('nickName', response.nickName)
      setValue('email', response.email)
      setValue('firstName', response.firstName)
      setValue('lastName', response.lastName)
    }
    // reset()
  }

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
                message: 'Минимум 3 символовa',
              },
            })}
            className={s.formInput}
            placeholder="Doe"
          />
          {errors?.nickName && <span style={{ color: 'red' }}>{errors?.nickName?.message || 'поле не заполненно'}</span>}
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
                message: 'Минимум 3 символовa',
              },
            })}
            className={s.formInput}
            placeholder="email@email.com"
          />
          {errors?.email && <span style={{ color: 'red' }}>{errors?.email?.message || 'поле не заполненно'}</span>}
        </div>

        <div>
          <label className={s.formLabel} htmlFor="firstname">
            Имя
          </label>
          <input
            {...register('firstName', {
              required: true,
              minLength: {
                value: 3,
                message: 'Минимум 3 символовa',
              },
            })}
            className={s.formInput}
            placeholder="John"
          />
          {errors?.firstName && <span style={{ color: 'red' }}>{errors?.firstName?.message || 'поле не заполненно'}</span>}
        </div>

        <div>
          <label className={s.formLabel} htmlFor="lastname">
            Фaмилия
          </label>
          <input
            {...register('lastName', {
              required: true,
              minLength: {
                value: 3,
                message: 'Минимум 3 символовa',
              },
            })}
            className={s.formInput}
            placeholder="Doe"
          />
          {errors?.lastName && <span style={{ color: 'red' }}>{errors?.lastName?.message || 'поле не заполненно'}</span>}
        </div>
      </div>
      <input className={s.formBtn} type="submit" value="сохранить" disabled={!isValid} />
    </form>
  )
}

export default Profile
