import s from './purchases.module.scss'
import cn from 'classnames'
import ProfileItem from './(purchasesItem)/profileItem'
const PurchasesItem = () => {
  const rand = () => {
    return Math.floor(Math.random() * (1000 - 900 + 1) + 900)
  }

  return (
    <div className="col-12">
      <div className="table-responsive table-responsive--border">
        <table className={s.profile__table}>
          <thead>
            <tr>
              <th>№</th>
              <th>
                <a href="#">
                  Product{' '}
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <path d="M9.71,10.21,12,7.91l2.29,2.3a1,1,0,0,0,1.42,0,1,1,0,0,0,0-1.42l-3-3a1,1,0,0,0-1.42,0l-3,3a1,1,0,0,0,1.42,1.42Zm4.58,4.58L12,17.09l-2.29-2.3a1,1,0,0,0-1.42,1.42l3,3a1,1,0,0,0,1.42,0l3-3a1,1,0,0,0-1.42-1.42Z" />
                  </svg>
                </a>
              </th>
              <th>
                <a href="#" className="active">
                  Title{' '}
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <path d="M17,13.41,12.71,9.17a1,1,0,0,0-1.42,0L7.05,13.41a1,1,0,0,0,0,1.42,1,1,0,0,0,1.41,0L12,11.29l3.54,3.54a1,1,0,0,0,.7.29,1,1,0,0,0,.71-.29A1,1,0,0,0,17,13.41Z" />
                  </svg>
                </a>
              </th>
              <th>
                <a href="#">
                  Platform{' '}
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <path d="M9.71,10.21,12,7.91l2.29,2.3a1,1,0,0,0,1.42,0,1,1,0,0,0,0-1.42l-3-3a1,1,0,0,0-1.42,0l-3,3a1,1,0,0,0,1.42,1.42Zm4.58,4.58L12,17.09l-2.29-2.3a1,1,0,0,0-1.42,1.42l3,3a1,1,0,0,0,1.42,0l3-3a1,1,0,0,0-1.42-1.42Z" />
                  </svg>
                </a>
              </th>
              <th>
                <a href="#" className="active">
                  Date{' '}
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <path d="M17,9.17a1,1,0,0,0-1.41,0L12,12.71,8.46,9.17a1,1,0,0,0-1.41,0,1,1,0,0,0,0,1.42l4.24,4.24a1,1,0,0,0,1.42,0L17,10.59A1,1,0,0,0,17,9.17Z" />
                  </svg>
                </a>
              </th>
              <th>
                <a href="#">
                  Price{' '}
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <path d="M9.71,10.21,12,7.91l2.29,2.3a1,1,0,0,0,1.42,0,1,1,0,0,0,0-1.42l-3-3a1,1,0,0,0-1.42,0l-3,3a1,1,0,0,0,1.42,1.42Zm4.58,4.58L12,17.09l-2.29-2.3a1,1,0,0,0-1.42,1.42l3,3a1,1,0,0,0,1.42,0l3-3a1,1,0,0,0-1.42-1.42Z" />
                  </svg>
                </a>
              </th>
              <th>
                <a href="#">
                  Status{' '}
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <path d="M9.71,10.21,12,7.91l2.29,2.3a1,1,0,0,0,1.42,0,1,1,0,0,0,0-1.42l-3-3a1,1,0,0,0-1.42,0l-3,3a1,1,0,0,0,1.42,1.42Zm4.58,4.58L12,17.09l-2.29-2.3a1,1,0,0,0-1.42,1.42l3,3a1,1,0,0,0,1.42,0l3-3a1,1,0,0,0-1.42-1.42Z" />
                  </svg>
                </a>
              </th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            {[1, 1, 1].map((_, id) => (
              <ProfileItem key={id} />
            ))}
          </tbody>
        </table>
      </div>
      <div className="col-12">
        <div className={s.paginator}>
          <div className={s.paginator__counter}>3 из 9</div>
          <ul className={s.paginator__wrap}>
            <li className={cn(s.paginator__item, s.paginator__item_prev)}>
              <a href="#">
                <svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512">
                  <polyline
                    points="244 400 100 256 244 112"
                    // style='fill:none;stroke-linecap:round;stroke-linejoin:round;stroke-width:48px'
                  />
                  <line
                    x1="120"
                    y1="256"
                    x2="412"
                    y2="256"
                    //  style='fill:none;stroke-linecap:round;stroke-linejoin:round;stroke-width:48px'
                  />
                </svg>
              </a>
            </li>
            <li className={cn(s.paginator__item, s.paginator__item_active)}>
              <a href="#">1</a>
            </li>
            <li className={s.paginator__item}>
              <a href="#">2</a>
            </li>
            <li className={s.paginator__item}>
              <a href="#">3</a>
            </li>
            <li className={cn(s.paginator__item, s.paginator__item_next)}>
              <a href="#">
                <svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512">
                  <polyline
                    points="268 112 412 256 268 400"
                    // style='fill:none;stroke-linecap:round;stroke-linejoin:round;stroke-width:48px'
                  />
                  <line
                    x1="392"
                    y1="256"
                    x2="100"
                    y2="256"
                    // style='fill:none;stroke-linecap:round;stroke-linejoin:round;stroke-width:48px'
                  />
                </svg>
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  )
}

export default PurchasesItem
