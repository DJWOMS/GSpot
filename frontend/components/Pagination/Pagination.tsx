'use client'

import React from 'react'
import ReactPaginate from 'react-paginate'
import { IconArrowLeft, IconArrowRight } from '@tabler/icons-react'
import style from './Pagination.module.scss'

const Pagination = () => {
  return (
    <ReactPaginate
      // css settings
      containerClassName={style.container}
      pageClassName={style.item}
      activeClassName={style.itemActive}
      breakClassName={style.item}
      previousClassName={style.linkBtn}
      nextClassName={style.linkBtn}
      previousLabel={<IconArrowLeft size={20} />}
      nextLabel={<IconArrowRight size={20} />}
      // settings ReactPaginate
      onPageChange={(event) => console.log(event)}
      pageRangeDisplayed={5}
      pageCount={100}
      renderOnZeroPageCount={null}
      // additional css settings
      pageLinkClassName={style.linkBtn}
      previousLinkClassName={style.linkBtn}
      nextLinkClassName={style.linkBtn}
      activeLinkClassName={style.activeLink}
      breakLinkClassName={style.linkBtn}
    />
  )
}

export default Pagination
