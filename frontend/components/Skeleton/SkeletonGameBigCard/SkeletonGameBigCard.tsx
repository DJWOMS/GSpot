import s from './SkeletonGameBigCard.module.scss'

const SkeletonGameBigCard = () => {
  return (
    <div className={s.card}>
      <div className={s.cardImg} />
      <div className={s.cardInfo}>
        <div className={s.cardInfoTitle} />
        {[...new Array(3)].map((_, index) => (
          <div className={s.cardInfoText} key={index} />
        ))}
        <div className={s.cardInfoTitle} />
        <div className={s.cardInfoBtn} />
      </div>
    </div>
  )
}

export { SkeletonGameBigCard }
