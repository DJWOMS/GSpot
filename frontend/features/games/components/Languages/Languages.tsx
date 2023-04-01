import s from './Languages.module.scss'

const Languages = () => {
  return (
    <>
      <table className={s.languagesTable}>
        <tbody>
          <tr>
            <td></td>
            <th>Интерфейс</th>
            <th>Озвучка</th>
            <th>Субтитры</th>
          </tr>
          <tr>
            <th>русский</th>
            <td></td>
            <td></td>
            <td></td>
          </tr>
          <tr>
            <th>английский </th>
            <td></td>
            <td></td>
            <td></td>
          </tr>
          <tr>
            <th>aрмянский </th>
            <td></td>
            <td></td>
            <td></td>
          </tr>
          <tr>
            <th>aбхазский</th>
            <td></td>
            <td></td>
            <td></td>
          </tr>
        </tbody>
      </table>
      <a className={s.languages} href="">
        Посмотреть все поддерживаемые языки
        <span>(24)</span>
      </a>
    </>
  )
}

export { Languages }
