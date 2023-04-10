import Pagination from 'components/Pagination'
import { Purchase, PurchaseCardInterface } from 'features/profile'
import { fetchServerSide } from 'lib/fetchServerSide'
import s from './page.module.scss'

const PurchasesItem = async () => {
  const purhases = await fetchServerSide<PurchaseCardInterface[]>({
    path: '/profile/purchases',
  })

  return (
    <>
      <table className={s.purchases}>
        <thead>
          <tr>
            <th>№</th>
            <th>Product</th>
            <th>Title</th>
            <th>Platform</th>
            <th>Date</th>
            <th>Price</th>
            <th>Status</th>
            <th></th>
          </tr>
        </thead>
        <tbody>{purhases && purhases.map((purchase) => <Purchase key={purchase.title} {...purchase} />)}</tbody>
      </table>

      <Pagination />
    </>
  )
}

export default PurchasesItem
