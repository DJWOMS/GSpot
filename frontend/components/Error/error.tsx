'use client'

import s from './error.module.css'

export default function Error({
  error,
  reset,
  statusCode,
  textError,
}: {
  error: Error
  statusCode: string
  reset: () => void
  textError: string
}) {
  const onClickHandler = () => reset()

  return (
    <div className={s.errorsContainer}>
      {statusCode && <h5 className={s.statusCode}> {statusCode}</h5>}
      <p className={s.title}> {textError}</p>
      <p className={s.errorMessage}>{error.message}</p>
      <button className={s.btnError} onClick={onClickHandler}>
        Пробовать снова
      </button>
    </div>
  )
}
