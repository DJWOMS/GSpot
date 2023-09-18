'use client'

import cn from 'classnames'
import Link from 'next/link'
import Form from '../Form'
import s from '../Form.module.css'
import SocialBtn from '../SocialBtn'

const Signin = () => {
  return (
    <Form onSubmit={() => console.log('hello')}>
      <div className={s.signGroup}>
        <input className={s.signInput} type="text" placeholder="Введите username" />
      </div>

      <div className={s.signGroup}>
        <input className={s.signInput} type="email" placeholder="Введите email" />
      </div>

      <div className={s.signGroup}>
        <input className={s.signInput} type="password" placeholder="Введите пароль" />
      </div>

      <div className={cn(s.signGroup, s.signCheckbox)}>
        <input id="remember" />
        <label htmlFor="remember">Запомнить меня</label>
      </div>

      <button className={s.signBtn}>Авторизация</button>
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
    </Form>
  )
}

export default Signin
