import { FC } from 'react'
import s from './Comments.module.scss'
import { SingleComment } from './SingleComment'

const Comments: FC = () => {
  return (
    <div className={s.comments}>
      <div className={s.title}>
        <h4>Comments</h4>
        <span>1</span>
      </div>

      <ul className={s.list}>
        <SingleComment />
      </ul>

      <form action="#" className="form">
        <textarea id="text" name="text" className={s.input} placeholder="Add comment"></textarea>
        <button type="button" className={s.button}>
          Send
        </button>
      </form>
    </div>
  )
}

export { Comments }
