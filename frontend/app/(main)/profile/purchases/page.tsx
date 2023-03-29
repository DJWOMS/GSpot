import s from './page.module.scss'
import ProfileItem from 'features/profile/components/Purchases/Purchase'
import Pagination from 'components/Pagination'
import Link from 'next/link'
import { ArrowsUpDown } from 'tabler-icons-react'

const th = ['Product', 'Title', 'Platform', 'Date', 'Price', 'Status']
const PurchasesItem = () => {
  return (
    <div className={s.wrapper}>
      <div className={s.tableResponsive}>
        <table className={s.profileTable}>
          <thead>
            <tr>
              <th>№</th>
              {th.map((i, id) => (
                <th key={id}>
                  <Link href="#" key={id}>
                    {i} <ArrowsUpDown strokeWidth={0.2} size={24} />
                  </Link>
                </th>
              ))}
              <th></th>
            </tr>
          </thead>
          <tbody>
            {[1, 1, 1].map((_, id) => (
              <ProfileItem key={id} />
            ))}
          </tbody>
        </table>
      </div>
      <Pagination />
    </div>
  )
}

export default PurchasesItem
