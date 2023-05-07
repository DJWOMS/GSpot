'use client'

import React, { FC } from 'react'
import ReactPaginate from 'react-paginate'
import { IconArrowLeft, IconArrowRight } from '@tabler/icons-react'
import s from './Pagination.module.scss'

interface Props {
  onChange: () => void
}

const Pagination: FC<Props> = ({ onChange }) => {
  return (
    <div className={s.wrapper}>
      <div className={s.counter}>12 from 3</div>
      <ReactPaginate
        // css settings
        containerClassName={s.container}
        pageClassName={s.item}
        activeClassName={s.itemActive}
        breakClassName={s.item}
        previousClassName={s.linkBtn}
        nextClassName={s.linkBtn}
        previousLabel={<IconArrowLeft size={17} />}
        nextLabel={<IconArrowRight size={17} />}
        // settings ReactPaginate
        onPageChange={onChange}
        pageRangeDisplayed={5}
        pageCount={3}
        renderOnZeroPageCount={null}
        // additional css settings
        pageLinkClassName={s.linkBtn}
        previousLinkClassName={s.linkBtn}
        nextLinkClassName={s.linkBtn}
        activeLinkClassName={s.activeLink}
        breakLinkClassName={s.linkBtn}
      />
    </div>
  )
}

export default Pagination
