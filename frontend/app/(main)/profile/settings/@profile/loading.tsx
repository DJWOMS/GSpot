import { SkeletonInput } from 'components/Skeleton'
import s from '../page.module.css'

const Loading = () => {
  return (
    <form action="#" className={s.form}>
      <h4 className={s.formTitle}>Настройки профиля</h4>
      <div className={s.col}>
        <div>
          <label className={s.formLabel} htmlFor="username">
            Ник
          </label>
          <SkeletonInput height="44px" />
        </div>
        <div>
          <label className={s.formLabel} htmlFor="email">
            Email
          </label>
          <SkeletonInput height="44px" />
        </div>
        <div>
          <label className={s.formLabel} htmlFor="firstName">
            Имя
          </label>
          <SkeletonInput height="44px" />
        </div>
        <div>
          <label className={s.formLabel} htmlFor="lastName">
            Фaмилия
          </label>
          <SkeletonInput height="44px" />
        </div>
      </div>
    </form>
  )
}

export default Loading
