import s from './SkeletonSelect.module.scss'

const SkeletonSelect = () => {
  return (
    <div className={s.animate}>
      <div className={s.line} />
    </div>
  )
}

export { SkeletonSelect }
