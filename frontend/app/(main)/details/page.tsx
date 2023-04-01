import { IconHeart, IconPlayerPlay, IconArrowLeft, IconArrowRight } from '@tabler/icons-react'
import cn from 'classnames'
import Carousel from 'components/Carousel'
import Section from 'components/Section'
import { Platform } from 'features/games'
import s from './page.module.scss'

export default function Page() {
  return (
    <Section>
      <div className="container">
        <div className="-mx-41">
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
                    </li>
                  </ul>
                </div>
              </div>

              <div className={s.detailsGallery}>
                <div className={s.detailsCarousel}>
                  <Carousel
                    breakpoints={{
                      0: {
                        slidesPerView: 2,
                      },
                      576: {
                        slidesPerView: 2,
                      },
                      768: {
                        slidesPerView: 3,
                      },
                      1200: {
                        slidesPerView: 5,
                      },
                    }}
                  >
                    {[...new Array(10)].map((_, index) => (
                      <img key={index} src="https://picsum.photos/1020" alt="" />
                    ))}
                  </Carousel>
                </div>

                <button className={cn(s.detailsNav, s.left)} type="button">
                  <IconArrowLeft />
                </button>
                <button className={cn(s.detailsNav, s.right)} type="button">
                  <IconArrowRight />
                </button>
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
                  <Platform type="ps" />
                  <Platform type="xbox" />
                  <Platform type="win" />
                  <Platform type="ap" />
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
                  <div className="max-w-full flex-[0_0_100%]">
                    <div className={s.requirements}>
                      <button>Windows</button>
                      <button>Linux</button>
                      <button>Apple</button>
                      <div className={s.requirementsWindows}>
                        <span className={s.requirementsTitle}>Minimum requirements:</span>
                        <ul className={s.requirementsList}>
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
                        <ul className={s.requirementsList}>
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

                      <div className={s.requirementsLinux}>
                        <span className={s.requirementsTitle}>Minimum requirements:</span>
                        <ul className={s.requirementsList}>
                          <li>
                            <span>OS:</span> Ubuntu Unity , Ubuntu Budgie , Nitrux
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
                        <ul className={s.requirementsList}>
                          <li>
                            <span>OS:</span> Ubuntu Unity , Ubuntu Budgie , Nitrux
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

                      <div className={s.requirementsApple}>
                        <span className={s.requirementsTitle}>Minimum requirements:</span>
                        <ul className={s.requirementsList}>
                          <li>
                            <span>OS:</span> macOS: 10.6.8 - 13.2.1
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
                        <ul className={s.requirementsList}>
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
      </div>
    </Section>
  )
}
