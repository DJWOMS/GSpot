import { PurchaseTable, PurchaseCardInterface } from 'features/profile'
import { fetchServerSide } from 'lib/fetchServerSide'

const PurchasesItem = async () => {
  const purchases = await fetchServerSide<PurchaseCardInterface[]>({
    path: '/profile/purchases',
  })

  return <>{purchases && <PurchaseTable items={purchases} />}</>
}

export default PurchasesItem
