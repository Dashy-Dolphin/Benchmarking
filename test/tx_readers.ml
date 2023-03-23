open Kcas

let loop_count = try int_of_string Sys.argv.(1) with _ -> 36288
let mode = Mode.lock_free

(* Number of shared counters being used to try to cause interference *)
let n_counters = try int_of_string Sys.argv.(2) with _ -> 2
let op_per_domain = loop_count / n_counters

(* Counters are first initialized with a dummy location *)
let counter = Loc.make ~mode 0

(* Barrier used to synchronize counter threads and the accumulator thread *)
let barrier = Barrier.make n_counters

let counter_thread _ () =
  (* We allocate actual counter locations within the domain to avoid false sharing *)
  let tx ~xt = Xt.get ~xt counter in

  Barrier.await barrier;

  for _ = 1 to op_per_domain do
    (* Increment the accumulator to cause interference *)
    Xt.commit { tx };

    (* Delay for a bit.  If we don't delay enough, we can starve the accumulator. *)
    for _ = 1 to Random.int 1000 do
      Domain.cpu_relax ()
    done
  done

let () =
  List.init n_counters counter_thread
  |> List.map Domain.spawn |> List.iter Domain.join
