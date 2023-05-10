'use client'

import React, { FC } from 'react'
import { IconX } from '@tabler/icons-react'
import Table from 'components/Table'
import { Platform } from 'features/games/components'
import type { PlatformType } from 'features/games/types'
import Image from 'next/image'
import Link from 'next/link'
import type { CheckoutGameCardInterface } from '../../types'
import s from './CheckoutTable.module.css'

interface Props {
  games: CheckoutGameCardInterface[]
}

const CheckoutTable: FC<Props> = ({ games }) => {
  return (
    <Table
      className={s.table}
      columns={[
        {
          accessorKey: 'coverImg',
          header: 'Product',
          cell: ({ getValue }) => (
            <div className={s.cardImg}>
              <Image src={getValue() as string} width={240} height={340} alt="img" />
            </div>
          ),
        },
        {
          accessorKey: 'title',
          header: 'Title',
          accessorFn: (item) => [item.link, item.title],
          cell: ({ getValue }) => {
            const [link, title] = getValue() as [string, string]
            return <Link href={link}>{title}</Link>
          },
        },
        {
          accessorKey: 'platform',
          header: 'Platform',
          cell: ({ getValue }) => <Platform {...(getValue() as PlatformType)} />,
        },
        {
          accessorKey: 'price',
          header: 'Price',
          accessorFn: (item) => [item.currency, item.price],
          cell: ({ getValue }) => {
            const [currency, price] = getValue() as [string, number]
            return <span className={s.cardPrice}>{`${currency.toUpperCase()} ${price}`}</span>
          },
        },
        {
          accessorKey: 'action',
          header: '',
          cell: () => (
            <button className={s.cardDelete} type="button">
              <IconX />
            </button>
          ),
        },
      ]}
      data={games}
    />
  )
}

export default CheckoutTable
