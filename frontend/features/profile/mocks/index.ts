import randomItem from 'utils/randomItem'
import randomNum from 'utils/randomNumber'
import type { CheckoutGameCardInterface, PurchaseCardInterface } from '../types'

export const generateMockPurchaseCard = (): PurchaseCardInterface => ({
  id: randomNum(4),
  title: randomItem(['Some', 'The', 'Another', 'Other', 'Word', 'Word', 'World']),
  price: randomNum(4),
  status: 'confirmed',
  coverImg: `https://loremflickr.com/240/320/abstract?lock=${randomNum(4)}`,
  platform: {
    type: 'win',
  },
  date: 'Aug 22, 2021',
  currency: 'rub',
  link: '/details/id',
})

export const generateMockCheckoutGameCard = (props = {}): CheckoutGameCardInterface => ({
  id: randomNum(6),
  title: randomItem(['Warcraft', 'CS:GO', 'Dota 2', 'Cyperpank']),
  coverImg: `https://loremflickr.com/240/240/abstract?lock=${randomNum(4)}`,
  platform: {
    type: 'win',
  },
  link: '/details/id',
  price: randomNum(4),
  currency: 'rub',
  ...props,
})
