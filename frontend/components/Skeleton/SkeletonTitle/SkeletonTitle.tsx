import s from 'components/Skeleton/SkeletonTitle/SkeletonTitle.module.css'

const SkeletonTitle = () => {
  return (
    <div className={s.animate}>
      <div className={s.line} />
    </div>
  )
}

export default SkeletonTitle
