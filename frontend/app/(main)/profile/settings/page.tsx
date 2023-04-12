import s from './page.module.scss'

const Settings = () => {
  return (
    <div className={s.row}>
      <form action="#" className={s.form}>
        <h4 className={s.formTitle}>Настройки профиля</h4>

        <div className={s.col}>
          <div>
            <label className={s.formLabel} htmlFor="username">
              Ник
            </label>
            <input id="username" type="text" className={s.formInput} placeholder="User 123" />
          </div>

          <div>
            <label className={s.formLabel} htmlFor="email">
              Email
            </label>
            <input id="email" type="text" className={s.formInput} placeholder="email@email.com" />
          </div>

          <div>
            <label className={s.formLabel} htmlFor="firstname">
              Имя
            </label>
            <input id="firstname" type="text" className={s.formInput} placeholder="John" />
          </div>

          <div>
            <label className={s.formLabel} htmlFor="lastname">
              Фaмилия
            </label>
            <input id="lastname" type="text" className={s.formInput} placeholder="Doe" />
          </div>
        </div>

        <button className={s.formBtn} type="button">
          Сохранить
        </button>
      </form>

      <form action="#" className={s.form}>
        <h4 className={s.formTitle}>Поменять пароль</h4>

        <div className={s.col}>
          <div>
            <label className={s.formLabel} htmlFor="oldpass">
              Старый пароль
            </label>
            <input id="oldpass" type="password" className={s.formInput} placeholder="***" />
          </div>
          <div>
            <label className={s.formLabel} htmlFor="newpass">
              Новый пароль
            </label>
            <input id="newpass" type="password" className={s.formInput} placeholder="***" />
          </div>
          <div>
            <label className={s.formLabel} htmlFor="confirmpass">
              Подтвердить Новый пароль
            </label>
            <input id="confirmpass" type="password" className={s.formInput} placeholder="***" />
          </div>
        </div>

        <button className={s.formBtn}>Поменять</button>
      </form>
    </div>
  )
}

export default Settings
