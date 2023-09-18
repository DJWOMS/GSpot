import s from 'components/Skeleton/SkeletonCard/SkeletonCard.module.css'

const SkeletonCard = () => {
  return (
    <div className={s.card}>
      <div className={s.cardImg} />
      {[...new Array(2)].map((_, index) => (
        <div className={s.cardText} key={index} />
      ))}
      <div className={s.cardBtn} />
    </div>
  )
}

export default SkeletonCard
