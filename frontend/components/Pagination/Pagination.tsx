import { IconArrowLeft, IconArrowRight } from '@tabler/icons-react'
import Link from 'next/link'
import PropTypes from 'prop-types'
import s from './Pagination.module.scss'

interface PaginationProps {
  currentPage: number
  totalItems: number
  itemsPerPage: number
}

const Pagination: React.FC<PaginationProps> = ({ currentPage, totalItems, itemsPerPage }) => {
  // рассчитываем количество страниц
  const totalPages = Math.ceil(totalItems / itemsPerPage)

  // создаем массив страниц для отображения в пагинации
  const pages = Array.from({ length: totalPages }, (_, i) => i + 1)

  return (
    <div className="col-12">
      <div className={s.container}>
        <div className={s.counter}>
          {/* отображаем текущее и общее количество элементов */}
          {`${itemsPerPage * (currentPage - 1) + 1}-${Math.min(itemsPerPage * currentPage, totalItems)} of ${totalItems}`}
        </div>

        <ul className={s.wrapper}>
          {/* кнопка "назад" должна быть неактивной на первой странице */}
          <li className={s.item}>
            {currentPage === 1 ? (
              <IconArrowLeft className={s.disabled} />
            ) : (
              <Link href={`/catalog/${currentPage - 1}`} passHref>
                <span className={s.linkBtn}>
                  <IconArrowLeft />
                </span>
              </Link>
            )}
          </li>

          {/* создаем элементы списка страниц */}
          {pages.map((page) => (
            <li key={page} className={`${s.item} ${currentPage === page ? s.itemActive : ''}`}>
              <Link href={`/page/${page}`} passHref>
                <span className={s.linkBtn}>{page}</span>
              </Link>
            </li>
          ))}

          {/* кнопка "вперед" должна быть неактивной на последней странице */}
          <li className={s.item}>
            {currentPage === totalPages ? (
              <IconArrowRight className={s.disabled} />
            ) : (
              <Link href={`/catalog/${currentPage + 1}`} passHref>
                <span className={s.linkBtn}>
                  <IconArrowRight />
                </span>
              </Link>
            )}
          </li>
        </ul>
      </div>
    </div>
  )
}

Pagination.propTypes = {
  currentPage: PropTypes.number.isRequired,
  totalItems: PropTypes.number.isRequired,
  itemsPerPage: PropTypes.number.isRequired,
}

export default Pagination
