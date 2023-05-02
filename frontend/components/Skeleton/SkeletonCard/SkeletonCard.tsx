import s from './SkeletonCard.module.scss'

const SkeletonCard = () => {
  return (
    <div className={s.block}>
      <div className={s.blockImg} />
      <div className={s.blockText} />
      <div className={s.blockText} />
      <div className={s.blockBtn} />
    </div>
  )
}

export { SkeletonCard }
