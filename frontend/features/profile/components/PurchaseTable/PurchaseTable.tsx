'use client'

import { FC, useState } from 'react'
import { IconX } from '@tabler/icons-react'
import { PaginationState } from '@tanstack/react-table'
import Table from 'components/Table'
import type { PurchaseCardInterface } from 'features/profile/types'
import Image from 'next/image'
import Link from 'next/link'
import s from './PurchaseTable.module.css'

interface Props {
  items: PurchaseCardInterface[]
}

const PurchaseTable: FC<Props> = ({ items }) => {
  const [pagination, setPagination] = useState<PaginationState>({
    pageSize: 10,
    pageIndex: 0,
  })

  return (
    <Table
      className={s.purchases}
      data={items}
      navigation={{
        pagination,
        setPagination,
        pageCount: 10,
      }}
      columns={[
        {
          accessorKey: 'id',
          header: '№',
          accessorFn: (item) => [item.link, item.id],
          cell: ({ getValue }) => {
            const [link, id] = getValue() as [string, number]
            return <Link href={link}>{id}</Link>
          },
        },
        {
          accessorKey: 'coverImg',
          header: 'Product',
          cell: ({ getValue }) => {
            const coverImg = getValue() as string
            return (
              <div className={s.purchaseImage}>
                <Image src={coverImg} width={240} height={340} alt="image" />
              </div>
            )
          },
        },
        {
          accessorKey: 'title',
          header: 'Title',
        },
        {
          accessorKey: 'platform',
          header: 'Platform',
          accessorFn: (item) => item.platform.type,
        },
        {
          accessorKey: 'date',
          header: 'Date',
        },
        {
          accessorKey: 'price',
          header: 'Price',
          accessorFn: (item) => [item.currency, item.price],
          cell: ({ getValue }) => {
            const [currency, price] = getValue() as [string, number]
            return (
              <span className={s.purchasePrice}>
                {currency}
                {price}
              </span>
            )
          },
        },
        {
          accessorKey: 'status',
          header: 'Status',
          cell: ({ getValue }) => <span className={s.purchaseStatus}>{getValue() as string}</span>,
        },
        {
          accessorKey: 'action',
          header: '',
          cell: () => (
            <button className={s.purchaseDelete}>
              <IconX strokeWidth={0.3} />
            </button>
          ),
        },
      ]}
    />
  )
}

export default PurchaseTable
