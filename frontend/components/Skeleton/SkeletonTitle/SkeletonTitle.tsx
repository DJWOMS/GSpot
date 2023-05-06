import s from './SkeletonTitle.module.scss'

const SkeletonTitle = () => {
  return (
    <div className={s.animate}>
      <div className={s.line} />
    </div>
  )
}

export { SkeletonTitle }
