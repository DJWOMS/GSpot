import { PurchaseTable } from 'features/profile/components'
import type { PurchaseCardInterface } from 'features/profile/types'
import { fetchServerSide } from 'lib/fetchServerSide'

const PurchasesItem = async () => {
  const purchases = await fetchServerSide<PurchaseCardInterface[]>({
    path: '/profile/purchases',
  })

  return <>{purchases && <PurchaseTable items={purchases} />}</>
}

export default PurchasesItem
