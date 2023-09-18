import s from './SkeletonGameBigCard.module.css'

const SkeletonGameBigCard = () => {
  return (
    <div className={s.card}>
      <div className={s.cardImg} />
      <div className={s.cardInfo}>
        <div className={s.cardInfoTitle} />
        {[...new Array(3)].map((_, index) => (
          <div className={s.cardInfoText} key={index} />
        ))}
        <div className={s.cardInfoPrice} />
        <div className={s.cardInfoText} />
        <div className={s.cardInfoBtn} />
      </div>
    </div>
  )
}

export default SkeletonGameBigCard
