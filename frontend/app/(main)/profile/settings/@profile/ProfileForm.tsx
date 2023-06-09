'use client'

import { FC, useState } from 'react'
import Form from 'components/Form/Form'
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
    <Form
      fields={[
        {
          name: 'username',
          label: 'Ник',
          rules: {
            required: true,
            minLength: {
              value: 3,
              message: errorMessage,
            },
          },
          render: ({ field }) => <input {...field} type="text" placeholder="Doe" className={s.formInput} />,
        },
        {
          name: 'email',
          label: 'Email',
          rules: {
            required: true,
            minLength: {
              value: 3,
              message: errorMessage,
            },
          },
          render: ({ field }) => (
            <input {...field} type="text" className={s.formInput} placeholder="email@example.com" />
          ),
        },
        {
          name: 'firstName',
          label: 'Имя',
          rules: {
            required: true,
            minLength: {
              value: 3,
              message: errorMessage,
            },
          },
          render: ({ field }) => <input {...field} type="text" placeholder="John" className={s.formInput} />,
        },
        {
          name: 'lastName',
          label: 'Фамилия',
          rules: {
            required: true,
            minLength: {
              value: 3,
              message: errorMessage,
            },
          },
          render: ({ field }) => <input {...field} type="text" placeholder="Doe" className={s.formInput} />,
        },
      ]}
      title="Настройки профиля"
      onSubmit={onSubmitUser}
      btnText="Сохранить"
      config={{
        mode: 'onBlur',
        defaultValues: {
          username: '',
          email: '',
          firstName: '',
          lastName: '',
        },
      }}
    />
  )
}

export default ProfileForm
