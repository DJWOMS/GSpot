import { IconArrowsUpDown } from '@tabler/icons-react'
import Pagination from 'components/Pagination'
import ProfileItem from 'features/profile/components/Purchases/Purchase'
import Link from 'next/link'
import s from './page.module.scss'

const PurchasesItem = () => {
  return (
    <div className={s.wrapper}>
      <div className={s.tableResponsive}>
        <table className={s.profileTable}>
          <thead>
            <tr>
              <th>№</th>
              <th>
                Product
                <Link href="#">
                  <IconArrowsUpDown strokeWidth={0.2} size={24} />
                </Link>
              </th>
              <th>
                Title
                <Link href="#">
                  <IconArrowsUpDown strokeWidth={0.2} size={24} />
                </Link>
              </th>
              <th>
                Platform
                <Link href="#">
                  <IconArrowsUpDown strokeWidth={0.2} size={24} />
                </Link>
              </th>
              <th>
                Date
                <Link href="#">
                  <IconArrowsUpDown strokeWidth={0.2} size={24} />
                </Link>
              </th>
              <th>
                Price
                <Link href="#">
                  <IconArrowsUpDown strokeWidth={0.2} size={24} />
                </Link>
              </th>
              <th>
                Status
                <Link href="#">
                  <IconArrowsUpDown strokeWidth={0.2} size={24} />
                </Link>
              </th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            {[1, 1, 1].map((purchase, id) => (
              <ProfileItem
                key={id}
                //  {...purchase}
              />
            ))}
          </tbody>
        </table>
      </div>
      <Pagination />
    </div>
  )
}

export default PurchasesItem
