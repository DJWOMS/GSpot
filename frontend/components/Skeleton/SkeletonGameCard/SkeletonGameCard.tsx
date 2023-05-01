import s from './SkeletonGameCard.module.scss'

const SkeletonGameCard = () => {
  return (
    <div className={s.animate}>
      <div className={s.animateBlock}>
        <div className={s.animateBlockImg} />
        <div className={s.animateBlockText} />
        <div className={s.animateBlockText} />
        <div className={s.animateBlockBtn} />
      </div>
    </div>
  )
}

export { SkeletonGameCard }
