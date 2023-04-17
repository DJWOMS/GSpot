import { useEffect } from 'react'
import { useForm } from 'react-hook-form'
import { UserDataInterface } from 'features/profile'
import { fetchServerSide } from 'lib/fetchServerSide'
import s from './page.module.scss'

interface InputTypes {
  userName: string
  email: string
  firstName: string
  lastName: string
}
const Profile = () => {
  useEffect(() => {
    const loadData = async () => {
      const response = await fetchServerSide<UserDataInterface[]>({
        path: '/profile/settings',
      })
      console.log(response, 'response')
      // if (response) {
      // setState(response)
      // }
    }
    loadData()
  }, [])

  const {
    register,
    formState: { errors, isValid },
    handleSubmit,
    reset,
  } = useForm<InputTypes>({
    mode: 'onBlur',
  })

  const onSubmitUser = (data: any) => {
    alert(JSON.stringify(data))
    reset()
  }

  return (
    <form action="#" className={s.form} onSubmit={handleSubmit(onSubmitUser)}>
      <h4 className={s.formTitle}>Настройки профиля</h4>

      <div className={s.col}>
        <div>
          <label className={s.formLabel} htmlFor="username">
            Ник
          </label>
          <input
            {...register('userName', {
              required: true,
              minLength: {
                value: 3,
                message: 'Минимум 3 символовa',
              },
            })}
            className={s.formInput}
            placeholder="Doe"
          />
          {errors?.userName && <span style={{ color: 'red' }}>{errors?.userName?.message || 'поле не заполненно'}</span>}
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
