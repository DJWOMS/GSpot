'use client'

import s from './Error.module.css'

export default function Error({ reset, textError }: { reset: () => void; textError: string }) {
  const onClickHandler = () => reset()

  return (
    <div className={s.errorsContainer}>
      <p className={s.title}> {textError}</p>
      <button className={s.btnError} onClick={onClickHandler}>
        Пробовать снова
      </button>
    </div>
  )
}
