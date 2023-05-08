import Section from 'components/Section'
import { CheckoutCouponForm, CheckoutForm, CheckoutGameCard, CheckoutGameCardInterface } from 'features/profile'
import { fetchServerSide } from 'lib/fetchServerSide'
import s from './page.module.css'

const CheckoutPage = async () => {
  const games = await fetchServerSide<CheckoutGameCardInterface[]>({
    path: '/profile/checkout',
  })

  return (
    <>
      <Section title="Checkout" />

      <Section>
        <div className={s.row}>
          <div className={s.left}>
            <div className={s.checkout}>
              <table className={s.checkoutTable}>
                <colgroup>
                  <col style={{ width: '15%' }} />
                  <col style={{ width: '35%' }} />
                  <col style={{ width: '10%' }} />
                  <col style={{ width: '20%' }} />
                  <col style={{ width: '10%' }} />
                </colgroup>

                <thead>
                  <tr>
                    <th scope="col">Product</th>
                    <th scope="col">Title</th>
                    <th scope="col">Platform</th>
                    <th scope="col">Price</th>
                    <th scope="col"></th>
                  </tr>
                </thead>

                <tbody>{games && games.map((game) => <CheckoutGameCard key={game.id} {...game} />)}</tbody>
              </table>

              <div className={s.checkoutInfo}>
                <div className={s.checkoutTotal}>
                  <p>Total:</p>
                  <span>$27.98</span>
                </div>
              </div>
            </div>
          </div>
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
