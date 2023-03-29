import s from './profileItem.module.scss'

const ProfileItem = () => {
  const rand = () => {
    return Math.floor(Math.random() * (1000 - 900 + 1) + 900)
  }
  return (
    <tr>
      <td>
        <a href="#modal-info" className="open-modal">
          8451
        </a>
      </td>
      <td>
        {/* <div className={s.profile__img} style={{"width":"40px", "height":"40px"}}> */}
        <img src={`https://picsum.photos/${rand()}`} alt="image" style={{ width: '80px', height: '80px', padding: '10px', marginLeft: '40px' }} />
        {/* </div> */}
      </td>
      <td>Desperados III Digital Deluxe Edition</td>
      <td>XBOX</td>
      <td>Aug 22, 2021</td>
      <td>
        <span className={s.profile__price}>$49.00</span>
      </td>
      <td>
        <span className={s.profile__status}>Not confirmed</span>
      </td>
      <td>
        <button className={s.profile__delete} type="button">
          <svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512">
            <line
              x1="368"
              y1="368"
              x2="144"
              y2="144"
              // style='fill:none;stroke-linecap:round;stroke-linejoin:round;stroke-width:32px'
            />
            <line
              x1="368"
              y1="144"
              x2="144"
              y2="368"
              // style='fill:none;stroke-linecap:round;stroke-linejoin:round;stroke-width:32px'
            />
          </svg>
        </button>
      </td>
    </tr>
  )
}

export default ProfileItem
