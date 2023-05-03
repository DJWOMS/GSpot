import { SkeletonInput } from 'components/Skeleton/SkeletonInput'
import s from './SkeletonGameBigCard.module.scss'

const SkeletonGameBigCard = () => {
  return (
    <div className={s.block}>
      <div className={s.blockImg} />
      <div className={s.blockInfo}>
        {[...new Array(4)].map((_, index) => (
          <div className={s.blockInfoText} key={index} />
        ))}
        <div className={s.blockInfoBtn} />
      </div>
    </div>
  )
}

export { SkeletonGameBigCard }
