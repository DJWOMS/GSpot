import s from './SkeletonGameCard.module.scss'

const SkeletonGameCard = () => {
  return (
    <div className={s.block}>
      <div className={s.blockImg} />
      <div className={s.blockText} />
      <div className={s.blockText} />
      <div className={s.blockBtn} />
    </div>
  )
}

export { SkeletonGameCard }
