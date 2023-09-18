import { FC } from 'react'
import type { CommentInterface } from 'features/news/types'
import s from './Comments.module.css'
import { SingleComment } from './SingleComment'

type CommentsType = {
  children: CommentInterface[]
}

const Comments: FC<CommentsType> = ({ children }) => {
  return (
    <div className={s.comments}>
      <div className={s.title}>
        <h4>Comments</h4>
        <span>1</span>
      </div>

      <ul className={s.list}>
        {children.map((data, index) => (
          <SingleComment key={index}>{data}</SingleComment>
        ))}
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

export default Comments
