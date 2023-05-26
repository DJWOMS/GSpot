'use client'

import Form from '../Form'
import s from '../Form.module.css'

const Forgot = () => {
  return (
    <Form onSubmit={() => console.log('hello')}>
      <div className={s.signGroup}>
        <input className={s.signInput} type="text" placeholder="Введите ваш email" />
      </div>

      <button className={s.signBtn}>Продолжить</button>

      <span className={s.signText}>На указанный email будет отправлен код для сброса пароля.</span>
    </Form>
  )
}

export default Forgot
