import Section from 'components/Section'
import { CheckoutCouponForm, CheckoutForm, CheckoutTable, CheckoutGameCardInterface } from 'features/profile'
import { fetchServerSide } from 'lib/fetchServerSide'
import s from './page.module.css'

const CheckoutPage = async () => {
  const games = await fetchServerSide<CheckoutGameCardInterface[]>({
    path: '/profile/checkout',
  })

  return (
    <>
      <Section title="Checkout">
        <div className={s.row}>
          <div className={s.left}>{games && <CheckoutTable games={games} />}</div>

          <div className={s.right}>
            <CheckoutCouponForm />
            <CheckoutForm />
          </div>
        </div>
      </Section>
    </>
  )
}

export default CheckoutPage
