import { GameCardInterface } from 'features/games'
import { CheckoutGameCard } from 'features/games/components/CheckoutGameCard/CheckoutGameCard'
import { fetchServerSide } from 'lib/fetchServerSide'
import Link from 'next/link'
import s from './page.module.scss'

const Checkout = async () => {
  const data = await fetchServerSide<GameCardInterface[]>({
    path: '/games/cart',
  })
  return (
    <div className={s.checkoutWrapper}>
      <div className={s.checkoutCover}>
        <div className="px-6 py-4">
          <div className={s.checkoutText}>Your Order:</div>
          {data?.map((game, id) => (
            <CheckoutGameCard {...game} key={id} />
          ))}
          <div className="flex justify-between">
            <div>Subtotal:</div>
            <div>RUB 60.00</div>
          </div>
          <div className="flex justify-between">
            <div>Total:</div>
            <div>RUB 60.00</div>
          </div>
        </div>
        <div className="px-6 py-4">
          <input className={s.checkoutInput} id="name" type="text" placeholder="Name" />
          <input className={s.checkoutInput} id="email" type="text" placeholder="Email" />
          <input className={s.checkoutInput} id="address" type="text" placeholder="Address" />
          <input className={s.checkoutInput} id="city" type="text" placeholder="City" />
          <input className={s.checkoutInput} id="state" type="text" placeholder="State" />
          <input className={s.checkoutInput} id="zip" type="text" placeholder="Zip" />
        </div>
        <div className="px-6 py-4">
          <Link href="/success">
            <button className={s.checkoutButton}>Place Order</button>
          </Link>
        </div>
      </div>
    </div>
  )
}

export default Checkout
