import { IconBrandXbox, IconBrandWindows, IconBrandApple, IconHeart, IconPlayerPlay } from '@tabler/icons-react'
import cn from 'classnames'
import Section from 'components/Section'
import s from './page.module.scss'

export default function Page() {
  return (
    <Section first bg>
      <div className="container">
        <div className="flex flex-wrap -mx-4">
          <div className="flex-[0_0_100%]">
            <div className={s.details}>
              <div className={s.detailsHead}>
                <div className={s.detailsCover}>
                  <img src="https://picsum.photos/1021" alt="" />
                  <a href="http://www.youtube.com/watch?v=0O2aH4XLbto" className={s.detailsTrailer}>
                    <IconPlayerPlay />
                    <span>Watch trailer</span>
                  </a>
                </div>

                <div className={s.detailsWrap}>
                  <h3 className={s.detailsTitle}>BioShock Infinite Complete Edition</h3>

                  <ul className={s.detailsList}>
                    <li>
                      <span>Release date:</span> 03.24.2016
                    </li>
                    <li>
                      <span>Genres:</span> Action, Role Playing, Open World
                    </li>
                    <li>
                      <span>Developer:</span> Envato Game Dev
                    </li>
                    <li>
                      <span>Языки:</span>
                      <table className={s.iksweb}>
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
                      </table>
                      <a className={s.languages} href="">
                        Посмотреть все поддерживаемые языки
                        <span>(24)</span>
                      </a>
                    </li>
                  </ul>
                </div>
              </div>
              <div className={s.detailsGallery}>
                <div className={s.detailsCarousel} id="detailsCarousel">
                  <a href="img/details/1-1.jpg"></a>
                  <img src="https://picsum.photos/1020" alt="" />
                  <a href="img/details/2-2.jpg"></a>
                  <img src="https://picsum.photos/1022" alt="" />
                  <a href="img/details/3-3.jpg"></a>
                  <img src="https://picsum.photos/1023" alt="" />
                  <a href="img/details/4-4.jpg"></a>
                  <img src="https://picsum.photos/1024" alt="" />
                  <a href="img/details/5-5.jpg"></a>
                  <img src="https://picsum.photos/1025" alt="" />
                  <a href="img/details/6-6.jpg"></a>
                </div>

                <button className="detailsNav detailsNav_prev" data-nav="#detailsCarousel" type="button"></button>
                <button className="detailsNav detailsNav--next" data-nav="#detailsCarousel" type="button"></button>
              </div>
              <div className={s.detailsText}>
                <p>
                  There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected
                  humour, or randomised words which dont look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to
                  be sure there isnt anything embarrassing hidden in the middle of text.
                </p>
                <p>
                  All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator
                  on the Internet. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first
                  true generator on the Internet. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making
                  this the first true generator on the Internet.
                </p>
              </div>

              <div className={s.detailsCart}>
                <span className={s.detailsCartTitle}>Available on platforms:</span>
                <ul className={s.detailsPlatforms}>
                  <li className={s.xb}>
                    <IconBrandXbox />
                  </li>
                  <li className={s.wn}>
                    <IconBrandWindows />
                  </li>
                  <li className={s.ap}>
                    <IconBrandApple />
                  </li>
                </ul>

                <span className={s.detailsCartTitle}>PRICE</span>
                <div className={s.detailsPrice}>
                  <span>$15.36</span>
                  <s>$38.80</s>
                  <b>60% OFF</b>
                </div>

                <div className={s.detailsActions}>
                  <button className={s.detailsBuy}>Buy now</button>

                  <button className={s.detailsFavorite}>
                    <IconHeart />
                    Add to favorites
                  </button>
                </div>
              </div>

              <div className={s.detailsContent}>
                <div className="row-auto">
                  <div className="col-12 col-xl-4 order-xl-2">
                    <div className="requirements">
                      <span className="requirements__title">Minimum requirements:</span>
                      <ul className="requirements__list">
                        <li>
                          <span>OS:</span> Windows 7,Windows 8.1,Windows 10
                        </li>
                        <li>
                          <span>Processor:</span> Intel Core i5-2400s @ 2.5 GHz or AMD FX-6350 @ 3.9 GHz
                        </li>
                        <li>
                          <span>Memory:</span> 6 GB RAM
                        </li>
                        <li>
                          <span>Graphics:</span> NVIDIA GeForce GTX 660 or AMD R9 270 (2048 MB VRAM with Shader Model 5.0)
                        </li>
                        <li>
                          <span>Disk Space:</span> 42 GB available space
                        </li>
                        <li>Architecture: Requires a 64-bit processor and OS</li>
                        <li>
                          <span>API:</span> DirectX 11
                        </li>
                        <li>
                          <span>Miscellaneous:</span> Video Preset: Lowest (720p)
                        </li>
                      </ul>

                      <span className={s.requirementsTitle}>Recommended requirements:</span>
                      <ul className="requirements__list">
                        <li>
                          <span>OS:</span> Windows 7,Windows 8.1,Windows 10
                        </li>
                        <li>
                          <span>Processor:</span> Intel Core i5-2400s @ 2.5 GHz or AMD FX-6350 @ 3.9 GHz
                        </li>
                        <li>
                          <span>Memory:</span> 6 GB RAM
                        </li>
                        <li>
                          <span>Graphics:</span> NVIDIA GeForce GTX 660 or AMD R9 270 (2048 MB VRAM with Shader Model 5.0)
                        </li>
                        <li>
                          <span>Disk Space:</span> 42 GB available space
                        </li>
                        <li>Architecture: Requires a 64-bit processor and OS</li>
                        <li>
                          <span>API:</span> DirectX 11
                        </li>
                        <li>
                          <span>Miscellaneous:</span> Video Preset: Lowest (720p)
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </Section>
  )
}
