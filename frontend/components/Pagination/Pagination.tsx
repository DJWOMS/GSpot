'use client'

import React from 'react'
import ReactPaginate from 'react-paginate'
import { IconArrowLeft, IconArrowRight } from '@tabler/icons-react'
import style from './Pagination.module.scss'

const Pagination = () => {
  return (
    <ReactPaginate
      // css settings
      containerClassName={style.root}
      breakLabel="..."
      nextLabel={<IconArrowRight size={20} />}
      previousLabel={<IconArrowLeft size={20} />}
      // settings ReactPaginate
      onPageChange={(event) => console.log(event)}
      pageRangeDisplayed={5}
      pageCount={5}
      renderOnZeroPageCount={null}
    />
  )
}

export default Pagination
