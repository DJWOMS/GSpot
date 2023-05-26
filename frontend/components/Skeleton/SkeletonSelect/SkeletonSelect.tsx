import s from './SkeletonSelect.module.css'

const SkeletonSelect = () => {
  return (
    <div className={s.animate}>
      <div className={s.line} />
    </div>
  )
}

export default SkeletonSelect
