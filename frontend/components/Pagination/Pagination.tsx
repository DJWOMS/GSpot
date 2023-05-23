import React, { FC, useMemo } from 'react'
import { IconArrowLeft, IconArrowRight } from '@tabler/icons-react'
import Link from 'next/link'
import s from './Pagination.module.css'

interface Props {
  path: string
  currentPage: number
  query?: { [key: string]: string | string[] | undefined }
}
const Pagination: FC<Props> = ({ path, currentPage, query }) => {
  const pageCount = 5
  const visiblePageButtonsCount = 3
  const visiblePages = useMemo(() => {
    const halfCount = Math.floor(visiblePageButtonsCount / 2)
    let startPage = currentPage <= halfCount ? 1 : currentPage - halfCount
    const endPage = Math.min(startPage + visiblePageButtonsCount - 1, pageCount)
    if (endPage === pageCount) {
      startPage = Math.max(pageCount - visiblePageButtonsCount + 1, 1)
    }
    return Array.from({ length: endPage - startPage + 1 }, (_, i) => startPage + i)
  }, [currentPage, pageCount, visiblePageButtonsCount])

  return (
    <div className={s.wrapper}>
      <div className={s.counter}>{`${currentPage} from ${pageCount}`}</div>
      <ul className={s.container}>
        <li className={`${s.linkBtn} ${currentPage === 1 && s.disabledBtn}`}>
          <Link className={s.linkBtn} href={{ pathname: path, query: { page: currentPage - 1 } }}>
            {<IconArrowLeft size={17} />}
          </Link>
        </li>
        {visiblePages.map((pageNumber) => (
          <li key={pageNumber} className={`${s.item} ${currentPage === pageNumber && s.itemActive}`}>
            <Link
              href={{ pathname: path, query: query ? { ...query, page: pageNumber } : { page: pageNumber } }}
              className={s.linkBtn}
            >
              {pageNumber}
            </Link>
          </li>
        ))}
        <li className={`${s.linkBtn} ${currentPage === pageCount && s.disabledBtn}`}>
          <Link
            className={s.linkBtn}
            href={{
              pathname: path,
              query: { page: currentPage + 1 },
            }}
          >
            {<IconArrowRight size={17} />}
          </Link>
        </li>
      </ul>
    </div>
  )
}

export default Pagination
