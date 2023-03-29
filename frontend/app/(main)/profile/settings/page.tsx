import s from './settings.module.scss'

async function getData(): Promise<any[]> {
  const res = await fetch('http://localhost:3100/api/latest-games')
  if (!res.ok) {
    throw new Error('Failed to fetch data')
  }
  return res.json()
}

const Settings = () => {
  // const data = await getData()
  return (
    <div className={s.fade} id="tab-2" role="tabpanel">
      <form action="#" className={s.form}>
        <div className="row">
          <div className="col-12 col-md-6 col-lg-12 col-xl-6">
            <h4 className={s.form__title}>Profile details</h4>
          </div>

          <div className="col-12 col-md-6 col-lg-12 col-xl-6">
            <label className={s.form__label} htmlFor="username">
              Ник
            </label>
            <input id="username" type="text" name="username" className={s.form__input} placeholder="User 123" />
          </div>

          <div className="col-12 col-md-6 col-lg-12 col-xl-6">
            <label className={s.form__label} htmlFor="email">
              Email
            </label>
            <input id="email" type="text" name="email" className={s.form__input} placeholder="email@email.com" />
          </div>

          <div className="col-12 col-md-6 col-lg-12 col-xl-6">
            <label className={s.form__label} htmlFor="firstname">
              Имя
            </label>
            <input id="firstname" type="text" name="firstname" className={s.form__input} placeholder="John" />
          </div>

          <div className="col-12 col-md-6 col-lg-12 col-xl-6">
            <label className={s.form__label} htmlFor="lastname">
              Фaмилия
            </label>
            <input id="lastname" type="text" name="lastname" className={s.form__input} placeholder="Doe" />
          </div>

          <div className="col-12">
            <button className={s.form__btn} type="button">
              Сохранить
            </button>
          </div>
        </div>
      </form>
      <form action="#" className={s.form}>
        <div className="row">
          <div className="col-12">
            <h4 className={s.form__title}>Поменять пароль</h4>
          </div>

          <div className="col-12 col-md-6 col-lg-12 col-xl-6">
            <label className={s.form__label} htmlFor="oldpass">
              Старый пароль
            </label>
            <input id="oldpass" type="password" name="oldpass" className={s.form__input} />
          </div>

          <div className="col-12 col-md-6 col-lg-12 col-xl-6">
            <label className={s.form__label} htmlFor="newpass">
              Новый пароль
            </label>
            <input id="newpass" type="password" name="newpass" className={s.form__input} />
          </div>

          <div className="col-12 col-md-6 col-lg-12 col-xl-6">
            <label className={s.form__label} htmlFor="confirmpass">
              Подтвердить Новый пароль
            </label>
            <input id="confirmpass" type="password" name="confirmpass" className={s.form__input} />
          </div>

          <div className="col-12 col-md-6 col-lg-12 col-xl-6">
            <label className={s.form__label} htmlFor="select">
              Выбери опции
            </label>
            <select name="select" id="select" className={s.formSelect}>
              <option className={s.option} value="0">
                опция
              </option>
              <option className={s.option} value="1">
                опция 2
              </option>
              <option className={s.option} value="2">
                опция 3
              </option>
            </select>
          </div>

          <div className="col-12" style={{ marginTop: '20px' }}>
            <button className={s.form__btn} type="button">
              Поменять
            </button>
          </div>
        </div>
      </form>
    </div>
  )
}

export default Settings
