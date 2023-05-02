import { SkeletonInput } from 'components/Skeleton/SkeletonInput'
import s from './SkeletonGameBigCard.module.scss'

const SkeletonGameBigCard = () => {
  return (
    <div className={s.block}>
      <div className={s.blockImg} />
      <div className={s.blockInfo}>
        <div className={s.blockInfoText} />
        <div className={s.blockInfoText} />
        <div className={s.blockInfoText} />
        <div className={s.blockInfoText} />
        <div className={s.blockInfoBtn} />
      </div>
      <SkeletonInput size={'44'} />
    </div>
  )
}

export { SkeletonGameBigCard }
