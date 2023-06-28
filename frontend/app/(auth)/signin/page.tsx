'use client'

import { SubmitHandler, useForm } from 'react-hook-form'
import SocialBtn from 'app/(auth)/SocialBtn'
import { CheckBox, Input } from 'components/Form'
import Form from 'components/Form/Form'
import { fetchServerSide } from 'lib/fetchServerSide'
import Link from 'next/link'
import { useRouter } from 'next/navigation'
import s from './page.module.css'

interface FormProps {
  username: string
  password: string
  rememberMe: string
}

const SignIn = () => {
  const router = useRouter()
  const {
    reset,
    formState: { errors },
  } = useForm<FormProps>()
  const onSubmit: SubmitHandler<FormProps> = async (data) => {
    const response = await fetchServerSide({
      method: 'POST',
      path: '/auth/access',
      body: JSON.stringify(data),
    })
    if (response) {
      reset()
      router.push('/profile/purchases')
    }
  }
  const rules = {
    required: 'The field is required',
    minLength: { value: 2, message: 'Please, enter more than 2 characters!' },
    pattern: { value: /[A-Za-z]+/, message: 'Field is invalid!' },
  }
  const disabled = !!errors.username || !!errors.password

  return (
    <div className={s.signContent}>
      <div className={s.signForm}>
        <Form<FormProps>
          onSubmit={onSubmit}
          btnText="Авторизация"
          disabled={disabled}
          styleBtn={s.signBtn}
          config={{
            defaultValues: {
              username: '',
              password: '',
            },
          }}
          fields={[
            {
              name: 'username',
              rules: rules,
              render: ({ field }) => <Input {...field} type="text" placeholder="Введите логин" />,
            },
            {
              name: 'password',
              rules: rules,
              render: ({ field }) => <Input {...field} type="password" placeholder="Введите пароль" />,
            },
            {
              name: 'rememberMe',
              render: ({ field }) => <CheckBox {...field} label={'Запомнить меня'} />,
            },
          ]}
        />
        <div className={s.signAlternative}>
          <span className={s.signDelimiter}>или</span>

          <div className={s.signSocials}>
            <SocialBtn type="facebook" />
            <SocialBtn type="google" />
            <SocialBtn type="twitter" />
          </div>

          <span className={s.signText}>
            Еще нет аккаунта? <Link href="/signup">Регистрация</Link>
          </span>

          <span className={s.signText}>
            <Link href="/forgot">Забыли пароль?</Link>
          </span>
        </div>
      </div>
    </div>
  )
}

export default SignIn
