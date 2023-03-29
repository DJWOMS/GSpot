import s from './page.module.scss'

const Settings = () => {
  return (
    <div className={s.fade} id="tab-2" role="tabpanel">
      <form action="#" className={s.form}>
        <div>
          <h4 className={s.formTitle}>Profile details</h4>
          <label className={s.formLabel} htmlFor="username">
            Ник
          </label>
          <input id="username" type="text" name="username" className={s.formInput} placeholder="User 123" />
          <label className={s.formLabel} htmlFor="email">
            Email
          </label>
          <input id="email" type="text" name="email" className={s.formInput} placeholder="email@email.com" />
          <label className={s.formLabel} htmlFor="firstname">
            Имя
          </label>
          <input id="firstname" type="text" name="firstname" className={s.formInput} placeholder="John" />
          <label className={s.formLabel} htmlFor="lastname">
            Фaмилия
          </label>
          <input id="lastname" type="text" name="lastname" className={s.formInput} placeholder="Doe" />
          <button className={s.formBtn} type="button">
            Сохранить
          </button>
        </div>
      </form>
      <form action="#" className={s.form}>
        <div>
          <h4 className={s.formTitle}>Поменять пароль</h4>
          <label className={s.formLabel} htmlFor="oldpass">
            Старый пароль
          </label>
          <input id="oldpass" type="password" name="oldpass" className={s.formInput} />
          <label className={s.formLabel} htmlFor="newpass">
            Новый пароль
          </label>
          <input id="newpass" type="password" name="newpass" className={s.formInput} />
          <label className={s.formLabel} htmlFor="confirmpass">
            Подтвердить Новый пароль
          </label>
          <input id="confirmpass" type="password" name="confirmpass" className={s.formInput} />
          <label className={s.formLabel} htmlFor="select">
            Выбери опции
          </label>
          <select name="select" id="select" className={s.formSelect}>
            {[1, 1, 1].map((i, id) => (
              <option className={s.option} value={id} key={id}>
                опция {id && id}
              </option>
            ))}
          </select>
          <button className={s.formBtn}>Поменять</button>
        </div>
      </form>
    </div>
  )
}

export default Settings
